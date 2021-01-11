
class InvalidValue(Exception):
    """Raised when passed-in value is invalid"""

class BaseWizard:
    """
    Base class for Wizards
    """
    def _ask(self, option_name, user_hint, passed_in_value, default=None, options=()):
        if passed_in_value is not None:
            if options and passed_in_value not in options:
                raise InvalidValue(
                    "Cannot use '%s' as value for %s. Valid options are: %s" %
                    (passed_in_value, option_name, options))
            return passed_in_value

        options_hint = "%s " % str(options) if options else ""
        user_hint = user_hint if '\n' in user_hint else "(%s)" % user_hint

        value = None
        while not value:
            value = input("Please provide %s %s%s: " % (option_name, options_hint, user_hint)).strip()
            if value == "" and default is not None:
                value = default

            if options and value not in options:
                print("Invalid value. Please re-try.")
                value = None

        # print("Hint: For scripting use %s(%s='%s')\n" % (self.__class__.__name__, option_name, value))
        return value

    @classmethod
    def help(cls):
        print(cls.__doc__)
        print("Usage: wizards.%s().run()" % cls.__name__)
