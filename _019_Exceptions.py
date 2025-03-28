def div(a, b):
    print("Starting...")
    if b == 0:
        raise ValueError("Denominator should never be zero")
    res = a/b
    print("Returning...")
    return res

if __name__ == "__main__":
    try:
        print("Main [start]")
        print(f"{div(7, 0)=}")
        print("Main[end]")
    except Exception as ex:
        print(f"Exception2 {ex!r}")
    except ZeroDivisionError as ex:
        print(f"Handler for {ex}")
    except (ValueError, TypeError) as ex:
        # print(f"Exception {repr(ex)}")
        print(f"Exception1 {ex!r}")          # Same as above
    finally:
        pass
    print("Really end")
