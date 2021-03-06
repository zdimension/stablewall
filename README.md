# stablewall
Solution to the GKS 2020 Round C problem "Stable Wall"

## How it works

![](https://i.imgur.com/Oag9yYK.png?1)

### Step 1

Let <img src="https://latex.codecogs.com/svg.latex?\Sigma=\{Z,O,M,A\}"> be the set of letters and <img src="https://latex.codecogs.com/svg.latex?E=\{(A,O),(M,O),(O,Z)\}"> the set of directed dependencies between letters.

A dependency <img src="https://latex.codecogs.com/svg.latex?d=(a,b)"> is *redundant* (noted <img src="https://latex.codecogs.com/svg.latex?r(d)">) iff <img src="https://latex.codecogs.com/svg.latex?\{(a,x),(x,b)\}\subset{E}">.

Let <img src="https://latex.codecogs.com/svg.latex?\Sigma'=\Sigma\cup\{*\}"> where <img src="https://latex.codecogs.com/svg.latex?*"> refers to the "ground".

Let <img src="https://latex.codecogs.com/svg.latex?E'=\{d\in{E}\mid\lnot{r}(d)\}\cup\{(a,*)\mid{a}\in\Sigma,\nexists(x,y)\in{E},x=a\}">. In this case, <img src="https://latex.codecogs.com/svg.latex?E'=\{(A,O),(M,O),(O,Z),(Z,*)\}">. In this case, there were no *redundant* dependencies. The dependency <img src="https://latex.codecogs.com/svg.latex?(Z,*)"> was added to allow easier computation of the node degrees.

Let <img src="https://latex.codecogs.com/svg.latex?G"> denote the directed graph <img src="https://latex.codecogs.com/svg.latex?(\Sigma',E')">.

The input is valid iff <img src="https://latex.codecogs.com/svg.latex?G"> is acyclic.

![G](https://i.imgur.com/L2nOmiY.png?1)

The number of valid solutions is obtained using the expression <img src="https://latex.codecogs.com/svg.latex?n=\prod_{a\in\Sigma'}{d^{-}(a)!}">.

### Step 2

Let <img src="https://latex.codecogs.com/svg.latex?R^{+}"> denote the transitive closure of <img src="https://latex.codecogs.com/svg.latex?E">. We have <img src="https://latex.codecogs.com/svg.latex?R^{+}=\{(A,O),(A,Z),(M,O),(M,Z),(O,Z)\}">. Let <img src="https://latex.codecogs.com/svg.latex?a\preceq{b}:=(b,a)\notin{R^{+}}">

The valid solutions <img src="https://latex.codecogs.com/svg.latex?\Omega"> are the permutations of <img src="https://latex.codecogs.com/svg.latex?\Sigma"> ordered under <img src="https://latex.codecogs.com/svg.latex?\preceq">.

In other words, we have <img src="https://latex.codecogs.com/svg.latex?\Omega=\{(\sigma_i)_{\left\[1,\left|\Sigma\right|\right\]}\in{S}(\Sigma)\mid\forall{i}\in\left\[1,\left|\Sigma\right|-1\right\],\sigma_{i}\preceq\sigma_{i+1}\}"> (note that here <img src="https://latex.codecogs.com/svg.latex?\sigma"> is an ordered tuple and not a set).

### Step 3: Preprocessing

Let <img src="https://latex.codecogs.com/svg.latex?f\colon\Sigma\to\mathcal{P}(\Sigma)"> which returns the set of all nodes reachable from the specified node, i.e. all supporting letters for a specified letter with <img src="https://latex.codecogs.com/svg.latex?f(a)=\{b\mid(a,b)\in{R}^{+}\}"> (this can be done using DFS or recursive graph traversal), here we have

| <img src="https://latex.codecogs.com/svg.latex?a">  | <img src="https://latex.codecogs.com/svg.latex?f(a)"> |
| ------------- | ------------- |
| <img src="https://latex.codecogs.com/svg.latex?Z">  | <img src="https://latex.codecogs.com/svg.latex?\emptyset">  |
| <img src="https://latex.codecogs.com/svg.latex?O">  | <img src="https://latex.codecogs.com/svg.latex?\{Z\}"> |
| <img src="https://latex.codecogs.com/svg.latex?M">  | <img src="https://latex.codecogs.com/svg.latex?\{O,Z\}">  |
| <img src="https://latex.codecogs.com/svg.latex?A">  | <img src="https://latex.codecogs.com/svg.latex?\{O,Z\}">  |

### Step 4: Processing
1. While there are letters yet to be added to the answer:
   1. Find the first one whose supporting letters are all already present, and add it. 
   2. If no such letter is found, halt. There is a cycle in the directed graph, which means two letters are codependent. Thus, there is no solution.
