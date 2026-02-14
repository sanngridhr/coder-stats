from io import BytesIO
from typing import Annotated

import matplotlib.pyplot as plt
from aiocache import cached
from fastapi import Depends, Response
from matplotlib.figure import Figure
from matplotlib.patches import Circle

PIE_RADIUS = 1.0
PIE_GAP = 0.05
PIE_WIDTH = 0.2

PIE_COLOURS = [
    "#AF3029",  # red
    "#BC5215",  # orange
    "#AD8301",  # yellow
    "#66800B",  # green
    "#24837B",  # cyan
    "#205EA6",  # blue
    "#5E409D",  # purple
    "#A02F6F",  # magenta
]
PIE_COLOURS_LEN = len(PIE_COLOURS)


class DataVisService:
    @cached(ttl=300, noself=True)
    async def to_svg(self, fig: Figure) -> Response:
        buffer: BytesIO = BytesIO()

        fig.savefig(fname=buffer, format="svg")
        plt.close(fig)

        svg_bytes: bytes = buffer.getvalue()
        return Response(content=svg_bytes, media_type="image/svg+xml")

    @cached(ttl=300, noself=True)
    async def get_donut_chart(self, data: dict[str, int | float]) -> Figure:
        fig, ax = plt.subplots()

        lumped_data: dict[str, int | float] = await self.__lump_small_data(data)
        keys: list[str] = list(lumped_data.keys())
        values: list[int | float] = list(lumped_data.values())

        ax.pie(
            x=values,
            labels=keys,
            radius=PIE_RADIUS,
            colors=PIE_COLOURS,
            counterclock=False,
            startangle=90,
            wedgeprops={"width": PIE_WIDTH, "edgecolor": "#FFFCF0"},
            explode=[PIE_GAP] * len(values),
        )

        ax.add_artist(Circle(xy=(0, 0), radius=PIE_RADIUS - PIE_WIDTH, fc="#FFFCF0"))

        return fig

    async def __lump_small_data(
        self,
        data: dict[str, int | float],
        major_num=(PIE_COLOURS_LEN - 1),
    ) -> dict[str, int | float]:
        major: dict[str, int | float] = {k: v for k, v in list(data.items())[:major_num]}
        minor_sum: int | float = sum(v for v in list(data.values())[major_num + 1 :])

        if minor_sum > 0:
            major["Other"] = minor_sum

        return major


type DataVisServiceDependency = Annotated[DataVisService, Depends()]
