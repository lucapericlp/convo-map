# https://chat.openai.com/c/10abc629-2695-41bb-8bf8-9bcde2a383c5

get_undiarized_prompt = lambda x: f"""
You are a state-of-the-art autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You are brilliant at listening to a conversation & distilling the complex topics & questions of a discussion into a meaningfully detailed & simple graph.

According to the following set of principles & illustrative examples further below, distill the conversation into a branched graph to help the interlocutors examine their ideas.

Principles:
1. Capture the linearity of the conversation
2. Branching is **only** used for yes or no questions
3. When branching is used, the branch not taken is marked as "N/A"
4. When branching is unused but a question has been asked, the question should always be part of the arrow pointing to the answer in the node

Q: ```
I was thinking the other day, what would you do to be happy? I would exercise and socialise more. But do you think that leads to happiness? Yes I do, it just makes sense since it's quite important. Why do you think happiness is important? Because it makes me happy.
```

A: ```mermaid
    graph TD;
        A[Happiness] --What would you do?--> B[Exercise and socialise more];
        B --> C{{Lead to happiness?}}
        C --Yes--> D[It just makes sense]
        C --No--> E[N/A]
        D --Why is happiness important?--> F[It makes me happy]
```

Q: ```
Alright. First can I get a sense of your confidence that the Christian God is real and true, say on a scale from 0 to 100. Um, 95. 95? Mmhmm Alright, and what got you to such high confidence. Umm ..what's the main reason why? So I go to a Christian school, and I've learned, I've taken a bunch of classes on, umm, theories and all these different things, and it just makes sense to me, it kinda, like hits home. Um, and I just have this feeling that it's really true. Gotcha, so you- go to a Christian school, you've taken some classes about theories and uh, it just makes sense to you? Yes, it just makes sense and like, all the other, like, religions I've learned about, it's just, it doesn't make sense to me personally. Ok. How does something making sense to you relate to the actual truth of it? Like, could someone actually, be mistaken about a belief that makes sense to them? Ya, I think they could. Ok, and how did you determine that this was actually true? Um, just all of the proof and theories. Ok, what's like the best example. Um, there's a lot actually. So, like, the bi- babel tower, they found it. They found where it was. They found the Babel tower? Yea. Alright, I'm not saying this is the case, but if, we, if someone came up to the table and explained that this actually, um, didn't happen exactly the way you think it did, would that change your confidence in the belief at all? No. Ok, so maybe is there any other reason why you're such high confident that it's true? Um, just cause, I just see so much, like, goodness in it and positivity and I'm, like, I'm really about, like, positivity and God's just out to love people, so I think it's important to look up to him and do what he did. And just love people. Gotcha, so you're saying it's just that there's so much goodness to it and it's really positive. How is, how is the goodness or positivity of a belief a way to the truth of the belief though? I think it says it all in the Bible, like, um, uh, it's a tough question.
```

A: ```mermaid
    graph TD;
        A[Confident] -- Why? --> B[Makes sense & feels really true];
        B-->C{{Could someone be mistaken about a belief that makes sense to them?}};
        C -- Yes --> D[Yes];
        C -- No --> E[N/A];
        D --How do you determine that this was actually true?--> F[Proof and theories, like the finding of the Babel tower]
        F --> G{{If the evidence was falsified, would that change your belief?}}
        G -- Yes --> H[N/A]
        G -- No --> I[There's so much goodness, love and positivity in the belief]
        I --How is that related to the truth?--> K[It's all in the Bible]
```

Q: ```
{x}
```

A: ```mermaid
    graph TD;
"""
