import json
import urllib2
import urllib
import md5

'''
Todas las funciones de la clase devuelven una variable con contenido JSON!
Deberas trabajar con ella para mostrar los datos que necesites en tu aplicacion.

Esto es asi para no limitar el uso de la clase y que el usuario pueda trabajar con todos los datos que
Tuenti nos envia a traves de su API.

Para inicializar una variable de la clase Tuenti debes indicar el SID (Session ID) que Tuenti usa para
hacer las peticiones. Puedes obtenerlo a traves de las cookies que usa Tuenti cuando estas logeado en Tuenti.com
Por el momento no se ha implementado ninguna funcion para identificar al usuario con su email y password, ya que la API
de Tuenti pide el "Application Key".


Tuenti for Python version 0.0.1
by @segura20101993
'''

class Tuenti:

    #Debes indicar el SID (Session ID). Para hacer peticiones a la API es necesario estar identificado.
    def __init__(self, SID):
        self.sid = SID
        self.API_Version = "0.7.1" #Se recomienda no modificar la version de la API.
        self.API = "http://api.tuenti.com/api/"

    #Devulve una variable JSON con toda la informacion del usuario cuyo ID coincide con el parametro "id".
    def getUsersData(self, id):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getUsersData",{"ids":[id],"fields":["name","surname","avatar","sex","status_post","phone_number","can_add_as_friend","can_send_message","favorite_books_rich","favorite_movies_rich","favorite_music_rich","favorite_quotes_rich","hobbies_rich","website","about_me_title","about_me","birthday","city","province","hometown","last_visit","visits","relationship","looking_for"]}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devuelve una variable JSON con todos los amigos del usuario autentificado con el SID y los datos de cada amigo.
    def getFriendsData(self):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getFriendsData",{"fields":["name","surname","sex","phone_number","mvno_subscriber"]}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Publica el estado indicado por la variable "status" al usuario autentificado con el SID.
    #Se devuelve en formato JSON si el estado se publico correctamente o no.
    def setUserStatus(self, status):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["setUserStatus",{"body":status}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con 20 fotos de la pagina indicada.
    #Ej: miTuenti.getAlbumPhotos(4444, 0) -> Devulve las primeras 20 fotos del usuario cuyo id es 4444.
    #Ej: miTuenti.getAlbumPhotos(4444, 1) -> Devulve las siguientes 20 fotos del usuario cuyo id es 4444.
    def getAlbumPhotos(self, id, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getAlbumPhotos",{"album_id":"tagged","page":page,"user_id":id,"photos_per_page":20}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devuelve una variable JSON con la informacion de los albums del usuario con el "id" indicado.
    #Si tiene mas de 20 albums, hay que ir pasando paginas.
    def getUserAlbums(self, id, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getUserAlbums",{"user_id":id,"page":page,"albums_per_page":20}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Envia el mensaje "message" al usuario con el id indicado. (Mensaje Privado)
    #Devuelve una variable JSON qye indica si se envio corretamente el mensaje o no.
    def sendMessage(self, id, message):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["sendMessage",{"body":message,"recipient":id,"legacy":"false"}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Envia el mensaje "message" al usuario con el id indicado en respuesta al hilo de mensajes indicado por "thread". (Mensaje Privado)
    #Devuelve una variable JSON qye indica si se envio corretamente el mensaje o no.
    def sendMessage(self, id, message, thread):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["sendMessage",{"body":message,"recipient":id,"legacy":"false", "thread_key":thread}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devuelve una variable JSON con la informacion de los 20 mensajes de la pagina indicada. BUZON DE ENTRADA
    #Hay que ir pasando la pagina para ver mas mensajes.
    def getInBox(self, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getInBox",{"page":page}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devuelve una variable JSON con la informacion de los 20 mensajes de la pagina indicada. BUZON DE SALIDA
    #Hay que ir pasando la pagina para ver mas mensajes.
    def getSentBox(self, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getSentBox",{"page":page}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devuelve una variable JSON con la informacion de los 20 mensajes de la pagina indicada. BUZON DE DESCONOCIDOS
    #Hay que ir pasando la pagina para ver mas mensajes.
    def getSpamBox(self, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getSpamBox",{"page":page}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con las notificaciones del usuario autentificado.
    def getUserNotifications(self):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getUserNotifications",{"max_notifications":20,"types":["new_commented_status","new_friend_requests", "unread_friend_messages","unread_spam_messages","new_profile_wall_posts","new_friend_requests","accepted_friend_requests","new_photo_wall_posts","new_tagged_photos","new_event_invitations","new_group_page_invitations","group_admin_promotions","group_member_promotions","mentions_bare","like_photos","like_posts_bare"]}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con los eventos proximos del usuario.
    def getUpcomingEvents(self):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["getUpcomingEvents",{"desired_number":20,"include_friend_birthdays":"true"}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con los resultados de la busqueda de PERSONAS usando la palabra "word"
    #Hay que ir pasando paginas para ir obteniendo mas resultados (20 por pagina)
    def searchPeople(self, word, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["search",{"results_per_page":20,"page":page,"category":"people","filters":{"scope":"all"},"string":word}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con los resultados de la busqueda de LUGARES usando la palabra "word"
    #Hay que ir pasando paginas para ir obteniendo mas resultados (20 por pagina)
    def searchPlaces(self, word, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["search",{"results_per_page":20,"page":page,"category":"places","filters":{"scope":"all"},"string":word}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Devulve una variable JSON con los resultados de la busqueda de PAGINAS usando la palabra "word"
    #Hay que ir pasando paginas para ir obteniendo mas resultados (20 por pagina)
    def searchPages(self, word, page):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["search",{"results_per_page":20,"page":page,"category":"pages","filters":{"scope":"all"},"string":word}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Envia una peticion de amistad con el mensaje indicado al usuario con el id indicado.
    #Devulve si se envio correctamente la peticion.
    def sendFriendRequest(self, id, message):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["sendFriendRequest",{"user_id":id,"message":message}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Publica un comentario en el muro de un usuario con el id indicado
    #Devulve si se envio correctamente la peticion.
    def addPostToProfileWall(self, id, message):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["addPostToProfileWall",{"user_id":id,"body":message,"legacy":"false"}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Publica un comentario en el estado de un usuario. Se debe indicar tanto el id del usuario al que pertenece el estado como el id del estado a comentar.
    #Devulve si se envio correctamente la peticion.
    def addPostToProfileWall(self, id, statusID, message):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["addCommentToProfileWall",{"body":message,"post_id":statusID,"user_id":id,"legacy":"false"}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Da a me gusta a un estado. Se debe indicar el id del usuario al que pertenece el estado y el id del estado.
    #Devulve si se envio correctamente la peticion.
    def likeWallPost(self, id, statusID):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["likeWallPost",{"user_id":id,"post_id":statusID}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response

    #Elimina un "me gusta" de un estado. Se debe indicar el id del usuario al que pertenece el estado y el id del estado.
    #Devulve si se envio correctamente la peticion.
    def unlikeWallPost(self, id, statusID):
        data = {"session_id":self.sid,"version":self.API_Version,"requests":[["unlikeWallPost",{"user_id":id,"post_id":statusID}]]}
        req = urllib2.Request(self.API)
        response = urllib2.urlopen(req, json.dumps(data))
        response = json.load(response)
        return response
