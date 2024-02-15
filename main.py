from flet import *
from custom_checkbox import CustomCheckBox


def main(Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    RED = "#ff0000"

    circle = Stack(
        controls=[
            Container(width=100, height=100, border_radius=50, bgcolor="white12"),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=["#00000000", RED],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment="center",
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://media.licdn.com/dms/image/D4D35AQHjh7ZM9sWO9Q/profile-framedphoto-shrink_400_400/0/1704465190300?e=1708552800&v=beta&t=bAzlmOnG3TY0Zmg3e-6vSxoM6Z_RcEaszQF8s91qxTU",
                                ),
                            ),
                        )
                    ],
                ),
            ),
        ]
    )

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8,
            alignment=alignment.center_right,
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35, top_right=0, bottom_left=35, bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 25
        page_2.controls[0].scale = transform.Scale(
            1,
            alignment=alignment.center_right,
        )
        page_2.update()

    create_task_view = Container(
        content=Container(
            on_click=lambda _: Page.go("/"), height=40, width=40, content=Text("x")
        )
    )

    tasks = Column(
        height=400,
        scroll="auto",
        # controls=[
        # Container(height=50,width=300,bgcolor='red'),
        # Container(height=50,width=300,bgcolor='red'),
        # Container(height=50,width=300,bgcolor='red'),
        # Container(height=50,width=300,bgcolor='red')
        # ]
    )

    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor="black",
                padding=padding.only(left=20, top=20),
                border_radius=25,
                content=CustomCheckBox(
                    color=RED, label="Create a new task interesting"
                ),
            ),
        )

    categories_card = Row(scroll="auto")
    categories = ["Business", "Family", "Friends"]

    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor="black",
                height=110,
                width=170,
                border_radius=20,
                padding=15,
                content=Column(
                    controls=[
                        Text("40 Tasks"),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white",
                            border_radius=20,
                            padding=padding.only(right=i * 20),
                            content=Container(bgcolor="red"),
                        ),
                    ]
                ),
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            on_click=lambda e: shrink(e), content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ]
                        ),
                    ],
                ),
                Container(height=20),
                Text(value="What's up , Yavuzhan!"),
                Text(value="CATEGORİES"),
                Container(
                    padding=padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            right=25,
                            bottom=2,
                            icon=icons.ADD,
                            on_click=lambda _: Page.go("/create_task"),
                        ),
                    ]
                ),
            ]
        )
    )

    page_1 = Container(
        width=400,
        height=850,
        bgcolor="green",
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(
                    alignment="end",
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(left=13, top=13),
                            height=50,
                            width=50,
                            border=border.all(color="white", width=2),
                            on_click=lambda e: restore(e),
                            content=Text("<"),
                        )
                    ],
                ),
                Container(height=20),
                circle,
                Text("Yavuz\nİs", size=32, weight="bold"),
                Container(height=25),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color="white60"),
                        Text(
                            "Templates",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL, color="white60"),
                        Text(
                            "Categories",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CALCULATE_OUTLINED, color="white60"),
                        Text(
                            "Analytics",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Image(
                    src=f"/images/1.png",
                    width=300,
                    height=200,
                ),
                Text(
                    "Good",
                    color=FG,
                    font_family="poppins",
                ),
            ]
        ),
    )
    page_2 = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor="green",
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[first_page_contents]),
            )
        ],
    )
    container = Container(
        width=400,
        height=750,
        bgcolor="red",
        border_radius=35,
        content=Stack(controls=[page_1, page_2]),
    )
    pages = {
        "/": View(
            "/",
            [container],
        ),
        "/create_task": View(
            "create_task",
            [
                create_task_view,
            ],
        ),
    }

    Page.add(container)

    def route_change(route):
        Page.views.clear()
        Page.views.append(pages[Page.route])

    Page.on_route_change = route_change
    Page.go(Page.route)


app(target=main, view=WEB_BROWSER,assets_dir='assets')


#! flet -r main.py çalıştırma komutu
