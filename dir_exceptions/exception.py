
def try_executing(execute, catch, always=None):
    """Simple wrapper function that will try to run
    execute and will run catch for any type exception
    that is caught by Python by default

    catch(exp) should take in an exception
    always is optional and will always execute after
    the try block"""
    try:
        execute()
    except (EnvironmentError, ArithmeticError, EOFError, AssertionError, AttributeError, BlockingIOError,
            BrokenPipeError, BufferError, ChildProcessError, ConnectionAbortedError, ConnectionError, FileExistsError,
            FileNotFoundError, FloatingPointError, ImportError, ImportError, IndentationError, IndexError,
            InterruptedError, IOError, IsADirectoryError, KeyError, LookupError, MemoryError, ModuleNotFoundError,
            NameError, NotADirectoryError, NotImplementedError, OSError, OverflowError, PermissionError,
            ProcessLookupError, RecursionError, ReferenceError, RuntimeError, SyntaxError, SystemError, TabError,
            TimeoutError, TypeError, UnboundLocalError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError,
            UnicodeTranslateError, ValueError, WindowsError, ZeroDivisionError) as exc:
        catch(exc)
    finally:
        if always is not None:
            always()
