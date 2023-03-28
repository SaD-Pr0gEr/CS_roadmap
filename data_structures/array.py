"""
Memory allocation
    Static Memory Allocation
        When we declare variables, we actually are preparing all the variables that will be used, so that the compiler
        knows that the variable being used is actually an important part of the program that the user wants and not
        just a rogue symbol floating around. So, when we declare variables, what the compiler actually does is allocate
        those variables to their rooms (refer to the hotel analogy earlier). Now, if you see, this is being done before
        the program executes, you can’t allocate variables by this method while the program is executing.
    Dynamic Memory Allocation
        The mechanism by which storage/memory/cells can be allocated to variables during the run time is called Dynamic
        Memory Allocation (not to be confused with DMA!)
        Dynamic memory allocation is the process of assigning the memory space during the execution time or the run time.

    There are two types of available memories: stack and heap. Static memory allocation can only be done on stack
    whereas dynamic memory allocation can be done on both stack and heap. An example of dynamic allocation to be done
    on the stack is recursion where the functions are put into call stack in order of their occurrence and popped off
    one by one on reaching the base case.

    While allocating memory on heap we need to delete the memory manually as memory is not freed(deallocated) by the
    compiler itself even if the scope of allocated memory finishes(as in case of stack).
    To conclude the above topic, static memory is something that the compiler allocates in advance. While dynamic memory
    is something that is controlled by the program during execution. The program may ask more of it or may delete some
    allocated.

Arrays
    An array is a collection of items of the same variable type stored that are stored at contiguous memory locations.
    It’s one of the most popular and simple data structures and is often used to implement other data structures.
    Each item in an array is indexed starting with 0.
    However, the above declaration is static or compile-time memory allocation, which means that the array element’s
    memory is allocated when a program is compiled.

Arrays can be static or dynamic
Static:
    C/C++ -> int array[5] => Array will store 5 integers
    C/C++ -> int *array = new int[5] => Array will store 5 integers

Types of arrays
    One-dimensional array(1D arrays):
        You can imagine a 1d array as a row, where elements are stored one after another.
    Two-dimensional array(2D arrays):
        2-D Multidimensional arrays can be considered as an array of arrays or as a matrix
        consisting of rows and columns.
    Three-dimensional array(3D arrays):
        3-D Multidimensional arrays contains three dimensions, so it can be considered an
        array of two-dimensional arrays.

How do Dynamic arrays work?
    A Dynamic array (vector in C++, ArrayList in Java) automatically grows when we try to make an insertion and there
    is no more space left for the new item. Usually the area doubles in size. A simple dynamic array can be constructed
    by allocating an array of fixed-size, typically larger than the number of elements immediately required.
    The elements of the dynamic array are stored contiguously at the start of the underlying array, and the remaining
    positions towards the end of the underlying array are reserved, or unused. Elements can be added at the end of a
    dynamic array in constant time by using the reserved space until this space is completely consumed. When all space
    is consumed, and an additional element is to be added, the underlying fixed-sized array needs to be increased in
    size. Typically, resizing is expensive because you have to allocate a bigger array and copy over all of the elements
    from the array you have overgrown before we can finally append our item. Approach: When we enter an element in array
    but array is full then you create a function, this function creates a new array double size or as you wish and copy
    all element from the previous array to a new array and return this new array. Also, we can reduce the size of the
    array. and add an element at a given position, remove the element at the end default and at the position also.

Types of Array operations:
    Traversal: Traverse through the elements of an array.
    Insertion: Inserting a new element in an array.
    Deletion: Deleting element from the array.
    Searching:  Search for an element in the array.
    Sorting: Maintaining the order of elements in the array.
"""
