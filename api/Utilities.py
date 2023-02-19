


class Util:
    def requestToJSON(self,request,valArray=False):
        #creador Cristian Mendoza email: cristian@ag.tools
        #Recibe una solicitud en forma de diccionario
        #Regresa un diccionario a profundiadad si asi se requiere
        band=False
        # print("content",request.content_type,request.content_params)
        if request.method == 'GET':
            doc=dict(request.GET.lists())
        elif request.method == 'POST':
            doc=dict(request.POST.lists())
            if len(doc.items())==0:
                try:
                    doc = json.loads(request.body)
                except:
                    doc = {}
                band=True
        # print("doc",doc)
        if "csrfmiddlewaretoken" in doc:
            del doc["csrfmiddlewaretoken"]
        if "undefined" in doc:
            del doc["undefined"]
        if band:
            return doc
        #return doc
        json1={}
        for filtro,val in doc.items():
            filtro=filtro.replace("[]","") #quitamos los arreglos
            if not valArray and len(val)==1:
                val=val[0]
            if "[" not in filtro:
                json1[filtro]=val
            else:
                names=filtro.split("[")
                names.reverse()
                dic={names[0].replace("]",""):val}
                njson=self.dicStringToJSON(names[1:],copy.deepcopy(dic))
                if json1:
                    json1=self.mergeDictionary(json1,njson,json1,[])
                else:
                    json1=njson
                # keys=names[1].split("]")
                # #print("keys",keys,"names",names)
                # if json.get(names[0]):
                #     lfiltro=json[names[0]]
                #     lfiltro[keys]=val
                #     json[names[0]]=lfiltro
                # else:
                #     nfiltro={keys[0]:val}
                #     json[names[0]]=nfiltro
        ##print(json)
        return json1
