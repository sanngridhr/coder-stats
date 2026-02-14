from io import BytesIO
from typing import Annotated

import matplotlib.pyplot as plt
from aiocache import cached
from fastapi import Depends, Response
from matplotlib.figure import Figure
from matplotlib.patches import Circle


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
        radius: float = 1.0
        gap: float = 0.05
        width: float = 0.2

        fig, ax = plt.subplots()

        lumped_data: dict[str, int | float] = await self.__lump_small_data(data)
        keys: list[str] = list(lumped_data.keys())
        values: list[int | float] = list(lumped_data.values())

        ax.pie(
            x=values,
            labels=keys,
            radius=radius,
            wedgeprops={"width": width, "edgecolor": "#FFFCF0"},
            explode=[gap] * len(values),
        )

        ax.add_artist(Circle(xy=(0, 0), radius=radius - width, fc="#FFFCF0"))

        return fig

    async def __lump_small_data(self, data: dict[str, int | float], threshold: float = 3000) -> dict[str, int | float]:
        major: dict[str, int | float] = {k: v for k, v in data.items() if v >= threshold}
        minor_sum: int | float = sum(v for v in data.values() if v < threshold)

        if minor_sum > 0:
            major["Other"] = minor_sum

        return major


type DataVisServiceDependency = Annotated[DataVisService, Depends()]
