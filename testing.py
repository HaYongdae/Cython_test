import timeit

cy = timeit.timeit('example_cy.test(5)', setup = 'import example_cy', number =1000000)
py = timeit.timeit('example_py.test(5)', setup = 'import example_py', number =1000000)

print (cy,py)
print ('Cython is {}x faster'.format(py/cy))

