from io import BytesIO
from typing import Annotated, Any

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
    async def get_donut_chart(self, data: dict[str, Any]) -> Figure:
        RADIUS: float = 1.0
        GAP: float = 0.05
        WIDTH: float = 0.2

        fig, ax = plt.subplots()

        ax.pie(
            x=list(data.values()),
            labels=list(data.keys()),
            radius=RADIUS,
            wedgeprops={"width": WIDTH, "edgecolor": "white"},
            explode=[GAP] * len(data.values()),
            normalize=True,
        )

        ax.add_artist(Circle(xy=(0, 0), radius=RADIUS - WIDTH, fc="#F2F0E5"))

        return fig


type DataVisServiceDependency = Annotated[DataVisService, Depends()]
