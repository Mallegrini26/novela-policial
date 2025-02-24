label pantalla:

screen mapaPantalla:
    add "bg mapa-de-londres.png"

    #biblioteca
    imagebutton:
        xpos 1150
        ypos 550
        idle "boton_idle.png"
        hover "boton_hover.png"
        action Jump("decidir")


screen BotonVolver:
    imagebutton:
        xpos 100
        ypos 100
        idle "boton_idle.png"
        hover "boton_hover.png"
        action Jump("mapa")