nombre_archivo = input("Ingrese el nombre del archivo: ")

partes = nombre_archivo.rsplit(".", 1)

if len(partes) == 2:
    extension = partes[1]
else:
    extension = ""

mimes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

mime = mimes.get(extension, "application/octet-stream")
print(mime)