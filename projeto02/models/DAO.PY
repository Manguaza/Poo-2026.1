import json


class DAO:
    arquivo = ""
    classe_modelo = None
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            obj.id = max(o.id for o in cls.objetos) + 1
        else:
            obj.id = 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        id = int(id)
        for obj in cls.objetos:
            if int(obj.id) == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for index, existente in enumerate(cls.objetos):
            if int(existente.id) == int(obj.id):
                cls.objetos[index] = obj
                cls.salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        id = int(id)
        original_length = len(cls.objetos)
        cls.objetos = [obj for obj in cls.objetos if int(obj.id) != id]
        if len(cls.objetos) != original_length:
            cls.salvar()
            return True
        return False

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w") as f:
            json.dump([o.to_json() if hasattr(o, "to_json") else o.__dict__ for o in cls.objetos], f, indent=2)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open(cls.arquivo, mode="r") as f:
                dicts = json.load(f)
                for d in dicts:
                    d = {k[1:] if k.startswith("_") else k: v for k, v in d.items()}
                    obj = cls.classe_modelo(**d)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass
