from app.validators import Validator, Number, OneOf


"""
buns — can range from 2 to 3;
cheese — can range from 0 to 2;
tomatoes — can range from 0 to 3;
cutlets — can range from 1 to 3;
eggs — can range from 0 to 2;
sauce — can be ketchup, mayo, or burger.
"""
BUNS = Number(2, 3)
CHEESE = Number(0, 2)
TOMATOES = Number(0, 3)
CUTLETS = Number(1, 3)
EGGS = Number(0, 2)
SAUCE = OneOf(["ketchup", "mayo", "burger"])


class BurgerRecipe:
    buns = BUNS
    cheese = CHEESE
    tomatoes = TOMATOES
    cutlets = CUTLETS
    eggs = EGGS
    sauce = SAUCE

    def __init__(
        self,
        buns: int,
        cheese: int,
        tomatoes: int,
        cutlets: int,
        eggs: int,
        sauce: str,
    ) -> None:
        validations = {
            "buns": buns,
            "cheese": cheese,
            "tomatoes": tomatoes,
            "cutlets": cutlets,
            "eggs": eggs,
            "sauce": sauce,
        }
        for _name in self.__dict__.copy().keys():
            attr = self.__getattribute__(_name)
            if isinstance(attr, Validator):
                for key, value in validations.items():
                    if key == _name:
                        attr.__set_name__(key)
                        attr.validate(value)
