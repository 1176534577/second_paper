from now_used.algorithm.ComputationalNeuralDynamicsAlgorithm import paper_noise_free, paper_noise_constant, \
    paper_noise_random

try:
    paper_noise_free.main()
except Exception as e:
    print(e)

try:
    paper_noise_constant.main()
except Exception as e:
    print(e)

try:
    paper_noise_random.main()
except Exception as e:
    print(e)
