from holoscan.conditions import CountCondition
from holoscan.core import Application, Operator, OperatorSpec

# example from https://github.com/nvidia-holoscan/holoscan-sdk/blob/main/examples/hello_world/python/hello_world.py
class HelloWorldOp(Operator):
    """Simple hello world operator.

    This operator has no ports.

    On each tick, this operator prints out hello world messages.
    """

    def setup(self, spec: OperatorSpec):
        pass

    def compute(self, op_input, op_output, context):
        print("")
        print("Hello World!")
        print("")


# Now define a simple application using the operator defined above


class HelloWorldApp(Application):
    def compose(self):
        # Define the operators
        hello = HelloWorldOp(self, CountCondition(self, 1), name="hello")

        # Define the one-operator workflow
        self.add_operator(hello)


def main():
    app = HelloWorldApp()
    app.run()


if __name__ == "__main__":
    main()
