# the TestEnv environment is used to simply simulate the network
from flow.envs import TestEnv

# the Experiment class is used for running simulations
from flow.core.experiment import Experiment

# all other imports are standard
from flow.core.params import VehicleParams
from flow.core.params import NetParams
from flow.core.params import InitialConfig
from flow.core.params import EnvParams
from flow.core.params import SumoParams
from flow.scenarios import Scenario

net_params = NetParams(
    template={
        "net": "sn.net.xml",
        "rou": "sn.rou.xml"
    }
)

env_params = EnvParams()
sim_params = SumoParams(render=True)
vehicles = VehicleParams()

network = Scenario(
    name='Schloß-Neuhaus',
    net_params=net_params,
    vehicles=vehicles
)

env = TestEnv(
    env_params=env_params,
    sim_params=sim_params,
    network=network
)

exp = Experiment(env=env)
exp.run(1, 1000)