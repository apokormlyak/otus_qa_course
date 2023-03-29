class ListAllBreeds:
    """
    Класс для хранения схемы ответа на запрос /list/all/
    """
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "object",
                "items": {
                    "type": "array",
                    "items": {
                        "anyOf": [
                            {"type": "string"},
                            {"type": "null"}
                        ]
                    }
                },
                "status": {"type": "string"}
            }
        }
    }


class RandomImage:
    """
    Класс для проверки схемы ответа /image/random/
    """
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        }
    }


class RandomImageList:
    """
    Класс для проверки схемы ответа /image/random/n
    """
    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ]
                }
            },
            "status": {
                "type": "string"
            }
        }
    }


class Brewery:
    """
     Класс для проверки схемы ответа /breweries/
    """
    schema = {
        "type": "array",
        "items": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "address_1": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "address_2": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "address_3": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "city": {"type": "string"},
            "state_province": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "website_url": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "state": {"type": "string"},
            "street": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            }
        }
    }
