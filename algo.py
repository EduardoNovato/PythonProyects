
playlist_demo = [
    {
        "nombre": "Playlist 1",
        "canciones": [
            "Cancion 1",
            "Cancion 2",
            "Cancion 3",
            "Cancion 4",
            "Cancion 5",
        ]
    },
    {
        "nombre": "Playlist 2",
        "canciones": [
            "Cancion 1",
            "Cancion 2",
            "Cancion 3",
            "Cancion 4",
            "Cancion 5",
        ]
    }
]

playlist_array = []


def app():
    agregar_playlist = True
    while agregar_playlist:
        playlist = {"nombre": "", "canciones": []}
        nombre_playlist = input('Como desea nombrar la playlist: \r\n')

        if nombre_playlist:
            playlist["nombre"] = nombre_playlist

            playlist_retornada = agregar_canciones(playlist)
            playlist_array.append(playlist_retornada)

        nueva_playlist = input('Deseas añadir otro playlist? S/N: \r\n')

        if nueva_playlist.upper() == "N":
            agregar_playlist = False

    print('###################')
    print("Total Playlist: {}".format(len(playlist_array)))
    print(playlist_array)
    print('###################')


def agregar_canciones(playlist):
    agregar_cancion = True
    while agregar_cancion:
        pregunta = "Escribe 'X' para dejar de agregar canciones\nAgrega canciones para la playlist {}:\t".format(
            playlist["nombre"])

        cancion = input(pregunta)

        if cancion.upper() == "X":
            agregar_cancion = False
            # Dejar de agregar
            print("Finalizado")
        else:
            # agregar canciones
            playlist['canciones'].append(cancion)

            print("###################")
            print(playlist)
            print("###################")

    return playlist


app()
