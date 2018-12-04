from data_parsers import StaticDataParser
from pyknow import *

class EngineMixin:
    def dispatch(self, args):
        print ('dispatch %s' % (' '.join(args)))


class RuleBasedSystemImplementation:
    fact_string_code = '''
class %s(Fact):
    pass
    '''
    class_string_code_template = '''

class MyRuleBased(KnowledgeEngine, EngineMixin):
    %s

    '''

    rul_string_code_template = '''
    @Rule(%(patterns)s)
    def %(rule_name)s(self, %(extra_params)s):
        %(handler_code)}s
    '''

    def validate_data(self):
        msg = ''
        if hasattr(self, 'data') and self.data is not None and type(self.data) is dict:
            if 'config' in self.data:
                if not self.data['config'].get('involved_facts'):
                    msg.append('Must include fact classes.')
            else:
                msg.append('Missing field config.')
            if not self.data.get('rules'):
                msg.append('No rule declared.')
        else:
            msg.append('Data is not declared yet.')
        if msg:
            exc = Exception('Engine data validation error:\n')
            exc.message = '\n'.join(msg)
            raise exc

    def declair_facts(self):
        exec(''.join([self.fact_string_code % f for f in self.data['config']['involved_facts']]))






    def engine_factory(self):
        exec(self.class_string_code_template)
        self.engine = eval('MyRuleBased')()

    def __init__(self, **kwargs):
        self.engine = None
        self.data = kwargs['parser'].parse()
        self.validate_data()
        self.declair_facts()
        self.engine_factory()

    def engine(self):
        if not hasattr(self, 'engine') and self.engine is not None:
            raise Exception('Must parse rule data before build engine')

    def run(self, fact_data=''):
        if hasattr(self, 'engine') and self.engine is not None:
            self.engine.reset()
            self.engine.declare()
            self.engine.run()
        else:
            raise Exception('Must have core engine be for running system !')


if __name__ == '__main__':
    my_parser = StaticDataParser()
    my_implement = RuleBasedSystemImplementation(parser=my_parser)
    my_implement.run()
