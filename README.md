
docker run -it  -p 4000:4000 hispn
docker run -v $HOME/Code/hispn:/app -it  -p 4000:4000 hispn
bundle exec jekyll build
bundle exec jekyll serve --host 0.0.0.0 --incremental
gem install webrick
...
---
Free Energy Principle
---

The "Free Energy Principle" is a theoretical framework developed in the field of neuroscience and cognitive science by the British neuroscientist Karl Friston. It proposes a unifying perspective on brain function, perception, and action. The principle is often discussed in the context of the brain's role in processing information and minimizing uncertainty.

The central idea of the Free Energy Principle can be quite complex, but it can be broken down into several key concepts:

1. Inference and Prediction: The brain's primary function is to make inferences about the world. It does this by constantly generating predictions about sensory inputs, which are then compared to actual sensory data. The brain aims to minimize the discrepancy between its predictions and the actual sensory input.

2. Free Energy: In this context, "free energy" is a mathematical concept borrowed from statistical physics and information theory. It represents the difference between the brain's internal model of the world (its predictions) and the actual sensory input. Minimizing free energy means reducing the difference between what the brain expects to perceive and what it actually perceives.

3. Active Inference: The brain not only makes passive predictions but also takes actions to actively gather information that reduces free energy. In other words, it engages in actions that help confirm and refine its internal model of the world.

4. Perception as Hypothesis Testing: Perception, according to the Free Energy Principle, is seen as a form../hispn/_posts/clia of hypothesis testing. The brain constructs its best guess (hypothesis) about what is happening in the world based on sensory input and prior beliefs, and then it seeks to refine and verify these hypotheses.

5. Hierarchical Models: The brain is thought to use a hierarchical model of the world, where higher levels make more abstract and long-term predictions, while lower levels make more concrete, short-term predictions.

6. Learning and Adaptation: The brain continually updates its internal model of the world by learning from new experiences and adjusting its predictions and actions accordingly. This learning process helps the brain become more accurate in minimizing free energy.

Overall, the Free Energy Principle provides a theoretical framework for understanding how the brain processes information, perceives the world, and takes actions. It emphasizes the brain's role in minimizing surprise and uncertainty, and it has been applied in various fields, including neuroscience, psychology, and artificial intelligence, to gain insights into the workings of the mind and to develop models of intelligent behavior.