# Checklist

This is a python package that helps data science projects better align with
the [Design Justice Network principles](http://designjusticenetwork.org/network-principles).
This is accomplished via checklists. The checklist tries not to reduce  the complexity of "ethical machine learning" to a series of steps, but rather tries to help you manage this complexity.

Checklists are filled out in the command line. There are two ways of calling the checklist. Whenever you call `git push` the checklist will automatically be triggered. Additionally, if you type the command `checklist` in the command line, it will also trigger the checklist.

For more information on the background, explanation, and justification for this tool, please see the 3 short essays/blog posts available [here](https://github.com/JoshFeldman95/checklist/tree/master/posts).

# Installation

To install the checklist tool, run:

`pip install git+https://github.com/JoshFeldman95/checklist.git`.

**Recommended, but not required:**
Life is busy, so to remind you to complete the checklist, we recommend overriding the `git push` command so that when it is called, the checklist is triggered. You can always also trigger the checklist by typing `checklist` into the command line.

To override `git push`, put the following script in your `.bash_profile` and restart the terminal:

```
# adds checklist to git push
function git {
  if [[ "$1" == "push" && "$@" != *"--help"* ]]; then
    shift 1
    command checklist
    command git push "$@"
  else
    command git "$@"
  fi
}
```

# The Checklist
The checklist included in this package is as follows:

**WARNING 1**: Following this checklist in no way guarantees just outcomes.

**WARNING 2**: This checklist does not reduce the need for government regulation. "Governments need to regulate AI by expanding the powers of sector-specific agencies to oversee, audit, and monitor these technologies by domain" (AI NOW 2018 Report).


1.	**Missing perspectives:** We have a system to collaborate and build trust with community members, particularly historically marginalized community members, on an ongoing basis.
2.	**Diverse Team:** Our team is representative of the community we’re collaborating with and includes historically marginalized voices.
3.	**Community Collaboration:** We collaborated with community members on an ongoing basis to:
    -	see what is already working and whether we can help amplify these solutions,
    -	set the objectives for the project,
    -	identify sources of bias that might be introduced during data collection/survey design,
    -	define what successful/beneficial/just outcomes look like and what unsuccessful/harmful/unjust outcomes look like,
    -	select the inputs to our model and define our metrics,
    -	understand what types of explanations will be needed,
    -	identify and prevent unintended uses and abuse of the model,
    -	develop a system to identify if our model inflicts harm, and what should be done if this occurs.
4.	**Fair Compensation:** Those who created our data, infrastructure, and hardware were fairly compensated.
5.	**Privacy Best Practices:** We proactively considered the privacy of individuals in our training data and of our users (i.e. minimize exposure of personally identifiable information, only collect necessary information, encryption at rest and in transit, data deletion plan, etc.)
6.	**Consent:** If we are using data on human subjects, they have provided (a) Freely given, (b) Reversible, (c) Informed, (d) Enthusiastic, and (e) Specific consent.
7.	**Met Standards Set by Community:** We have assessed with community members whether our system meets the criteria they defined, disaggregated across intersecting identities (i.e. we meet the criteria not just for Black people and women, but also for Black women)
8.	**Honest and Intersectional Representation:** Our visualizations, summary statistics, and reports honestly illustrate outcomes across intersecting identities.
9.	**Roll back:** We have tested turning off or rolling back the model in production.
10.	**Auditability:** The process of generating the analysis is well documented and reproducible, and we have provided a method for the public sector and civil society to safely access our data and models.
11.	**Should This Exist:** We still think we should build this.
