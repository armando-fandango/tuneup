from tuneup.horserace import latex_horse_race
from tuneup.trivariatesingleobjectivesolvers.trivariateboxsolvers import OPEN_SOURCE_SOLVERS
from tuneup.trivariateobjectives.trivariateboxobjectives import OBJECTIVES
from pprint import pprint


def race_specification(debug:bool):
    solvers = OPEN_SOURCE_SOLVERS
    objectives = OBJECTIVES
    max_thresholds = 5 if debug else 20
    n_outer_repeat = 1000 if not debug else 5
    n_threshold_repeat = 10 if not debug else 1  # Number of times to call each solver when setting scoring scale
    n_trials = 50 if not debug else 10  # Number of evaluations of the objective function
    n_inner_repeat = 100 if not debug else 2  # Number of times to run the horse race
    max_objectives = 2 if debug else 10
    objectives = dict(reversed([(k, v) for k, v in objectives.items()][:max_objectives]))
    threshold_trials = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024][:max_thresholds]
    spec = {'objectives': objectives,
            'solvers': solvers,
            'threshold_trials': threshold_trials,
            'n_outer_repeat': n_outer_repeat,
            'n_threshold_repeat': n_threshold_repeat,
            'n_trials': n_trials,
            'n_inner_repeat': n_inner_repeat}
    return spec


if __name__=='__main__':
    spec = race_specification(debug=True)
    pprint(spec)
    latex_horse_race(**spec)