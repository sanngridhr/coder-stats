from io import BytesIO
from typing import Annotated, Mapping

import matplotlib.pyplot as plt
from fastapi import Depends, Response
from matplotlib.figure import Figure

from app.api.core.query_params.constants.enums import Direction
from app.api.core.query_params.models.piechart_query_params import PieChartQueryParams


class DataVisService:
    def to_svg(self, fig: Figure) -> Response:
        buffer: BytesIO = BytesIO()

        fig.savefig(fname=buffer, format="svg")
        plt.close(fig)

        svg_bytes: bytes = buffer.getvalue()
        return Response(content=svg_bytes, media_type="image/svg+xml")

    def get_donut_chart(self, data: Mapping[str, int | float], params: PieChartQueryParams) -> Figure:
        colours: list[str] = [c + params.theme_transparency for c in params.theme.get_colours()]
        if params.theme_reverse:
            colours.reverse()

        limit: int = len(colours) if params.limit is None else params.limit

        fig, ax = plt.subplots()

        cut_data: dict[str, int | float] = (
            self.__lump_small_data(data, limit)
            if params.lump_small_data
            else {k: v for k, v in list(data.items())[: limit - 1]}
        )
        keys: list[str] = list(cut_data.keys())
        values: list[int | float] = list(cut_data.values())

        ax.pie(
            x=values,
            labels=keys,
            radius=params.radius,
            colors=colours,
            counterclock=(params.direction == Direction.ANTICLOCKWISE),
            startangle=params.start_angle,
            textprops={"font": params.font},
            wedgeprops={"width": params.width},
            explode=[params.gap] * min(limit, len(values)),
        )

        return fig

    def __lump_small_data(
        self,
        data: Mapping[str, int | float],
        limit: int,
    ) -> dict[str, int | float]:
        major: dict[str, int | float] = {k: v for k, v in list(data.items())[: limit - 1]}
        minor_sum: int | float = sum(v for v in list(data.values())[limit:])

        if minor_sum > 0:
            major["Other"] = minor_sum

        return major


type DataVisServiceDependency = Annotated[DataVisService, Depends()]
