import random
import numpy as np


class Bandit:
    def __init__(self, payoff_probs):
        self.actions = range(len(payoff_probs))
        self.pay_offs = payoff_probs

    def sample(self, action):
        selector = random.random()
        # 1 or 0 are the rewards 
        return 1 if selector <= self.pay_offs[action] else 0


def optimal_agent(bandit, iterations):
    """Always choose the best action. This agent isn't realistic, because he has knowledge that other agents don't have.
    """
    a = np.argmax(bandit.pay_offs)
    actions = []
    rewards = []

    for _ in range(iterations):
        r = bandit.sample(a)
        actions.append(a)
        rewards.append(r)

    return actions, rewards


def explore_greedy_agent(bandit, iterations, initial_rounds=10, random_agent=False):
    """Initially explore initial_rounds times and then stick to the best action.
    """
    pay_offs = dict()
    best_action = -1
    actions = []
    rewards = []

    if random_agent:
        initial_rounds = iterations

    for t in range(iterations):
        # for the initial rounds pick a random action
        if t < initial_rounds:
            a = random.choice(bandit.actions)
            r = bandit.sample(a)

            # update rewards
            if a in pay_offs:
                pay_offs[a].append(r)
            else:
                pay_offs[a] = [r]
        # otherwise pick the best one thus far
        else:
            if (best_action == -1):
                # check for the action with the best average payoff
                mean_dict = {}
                for key,val in pay_offs.items():
                    mean_dict[key] = np.mean(val) 
                best_action = max(mean_dict, key=mean_dict.get)
            a = best_action
    
            r = bandit.sample(a)
        
        actions.append(a)
        rewards.append(r)

    return actions, rewards


def random_agent(bandit, iterations):
    """Call the initial explore agent with random_agent==True to choose every action at random.
    """
    return explore_greedy_agent(bandit, iterations, random_agent=True)
    

def epsilon_greedy_agent(bandit, iterations, epsilon=0.2, initial_rounds=10, decay=1, optimistic=False):
    """Use the epsilon-greedy algorithm by performing the action with the best average
    payoff with the probability (1-epsilon), otherwise pick a random action to keep
    exploring.
    """
    pay_offs = dict()
    actions = []
    rewards = []
    return actions, rewards


def decaying_epsilon_greedy_agent(bandit, iterations, epsilon=0.2, initial_rounds=1, decay=0.99):
    """Use epsilon greedy with decaying epsilon.
    """
    pay_offs = dict()
    actions = []
    rewards = []
    return actions, rewards


def optimistic_greedy_agent(bandit, iterations, epsilon=0.2, initial_rounds=1, decay=0.99):
    """Start with high initial Q values, to make the agent explore more in the beginning.
    """
    actions = []
    rewards = []
    return actions, rewards


def ucb_agent(bandit, iterations, c=0.3):
    """Uses the Q-value of the action (reward so far divided by the number of times chosen) as exploitation.
    Uses the c * square root of ln(t)/Nt(a) for exploration.
    """
    pay_offs = dict()
    actions = []
    rewards = []
    return actions, rewards


def thompson_agent(bandit, iterations):
    """Build up a probability model from the obtained rewards, and then samples from this to choose an action.
    The model provides a level of confidence in the rewards. Confidence increases as more samples are collected.
    """
    pay_offs = dict()
    actions = []
    rewards = []
    return actions, rewards
