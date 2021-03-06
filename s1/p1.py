from evo_strategy import ES
from cost_functions import rosen, ackely
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


## settings
n_dims = 5000
cost_func = rosen
iterations = 1000
consider_cov = True

es = ES(n_dims, cost_func)
es.evolve(iterations=iterations, consider_cov=consider_cov)
# es.plot_history(path='third_model_rosen.png')
es.save_history(path='third_model_cov_rosen')


n_dims = 1000
cost_func = ackely
iterations = 1000
consider_cov = True

es = ES(n_dims, cost_func)
es.evolve(iterations=iterations, consider_cov=consider_cov)
# es.plot_history(path='third_model_ackely.png')
es.save_history(path='third_model_cov_ackely')