import json

class DAO:
    arquivo = ""
    classe_modelo = None
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for index, existente in enumerate(cls.objetos):
            if existente.id == obj.id:
                cls.objetos[index] = obj
                cls.salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        original_length = len(cls.objetos)
        cls.objetos = [obj for obj in cls.objetos if obj.id != id]
        if len(cls.objetos) != original_length:
            cls.salvar()
            return True
        return False

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w") as f:
            json.dump([o.__dict__ for o in cls.objetos], f, indent=2)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open(cls.arquivo, mode="r") as f:
                dicts = json.load(f)
                for d in dicts:
                    obj = cls.classe_modelo(**d)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass