from pyknow import Fact, KnowledgeEngine, Rule, AND, watch, unwatch
from random import choice


class Money(Fact):
    """ ask about money you have """
    pass


class Ticket(Fact):
    """ ask about free ticker """


class Solution(KnowledgeEngine):
    @Rule(Ticket(ticket='yes'))
    def have_ticket(self):
        print('You can pass')


    @Rule(AND(Money(money='yes'), Ticket(ticket='yes')))
    def have_ticket_and_money(self):
        print('Lucky you')


    @Rule(AND(Money(money='yes'), Ticket(ticket='no')))
    def buy_ticket(self):
        print('Buy the ticket')


    @Rule(AND(Money(money='no'), Ticket(ticket='no')))
    def no_money_nor_ticket(self):
        print('Sorry no money no honey :<')


if __name__ == '__main__':
    engine = Solution()
    engine.reset()

    ask_money = input("Did you have money?: ")
    ask_ticket = input("Did you have free luanch ticket?: ")

    engine.declare((Money(money=ask_money)), (Ticket(ticket=ask_ticket)))

    watch()
    engine.run()
    unwatch()
