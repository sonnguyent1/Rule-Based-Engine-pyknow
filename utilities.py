from pyknow import Fact


def fact_factroy(name, **attributes):
    return type(name, Fact)(**attributes)


def knowledge_factory(rule_set):
    pass
