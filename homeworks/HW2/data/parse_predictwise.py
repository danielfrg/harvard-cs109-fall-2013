from BeautifulSoup import BeautifulSoup
import pandas as pd

data = open('predictwise.html').read()
bs = BeautifulSoup(data)

obama = {}
romney = {}
votes = {}

for state in bs.findAll('div', 'state_info'):
    name = state.find('h5').contents[0]
    v = state.find('dl', 'votes').find('dt').contents[0]
    o, r = state.findAll('dl', 'chance')
    votes[name] = int(v)
    obama[name] = float(o.find('dt').contents[0][:-1]) / 100
    romney[name] = float(r.find('dt').contents[0][:-1]) / 100



states = sorted(votes.keys())
votes = [votes[s] for s in states]
obama = [obama[s] for s in states]
romney = [romney[s] for s in states]

data = pd.DataFrame(dict(States=states, Votes=votes,
                         Obama=obama, Romney=romney))
data.to_csv('predictwise.csv', index=False)
