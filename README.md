# Starter Repo
This repo has everything you need to get started on the program, good luck!
<table class="ck-table-resized"><colgroup><col style="width: 25%;"><col style="width: 75%;"></colgroup><thead><tr><th>&nbsp;</th><th>Service criteria</th></tr></thead><tbody><tr><th>Capulet Engine</th><td>Once every 30,000 miles</td></tr><tr><th>Willoughby Engine</th><td>Once every 60,000 miles</td></tr><tr><th>Sternman Engine</th><td>Only when the warning indicator is on</td></tr><tr><th>Spindler Battery</th><td>Once every 2 years</td></tr><tr><th>Nubbin Battery</th><td>Once every 4 years</td></tr></tbody></table>
<table class="ck-table-resized"><colgroup><col style="width: 31.36%;"><col style="width: 36.23%;"><col style="width: 32.41%;"></colgroup><thead><tr><th>Car</th><th>Engine</th><th>Battery</th></tr></thead><tbody><tr><th>Calliope</th><td>Capulet Engine</td><td>Spindler Battery</td></tr><tr><th>Glissade</th><td>Willoughby Engine</td><td>Spindler Battery</td></tr><tr><th>Palindrome</th><td>Sternman Engine</td><td>Spindler Battery</td></tr><tr><th>Rorschach</th><td>Willoughby Engine</td><td>Nubbin Batte</td></tr><tr><th>Thovex</th><td>Capulet Engine</td><td>Nubbin Battery</td></tr></tbody></table>

<h2>Task 4</h2>
Upgrade Spindler batteries
First, modify the Spindler battery so it requires service after three years instead of two.
Notice how easy it is to make this change - you only need to touch one line of code instead of several, and the place where that line of code lives should be immediately obvious.
Consider what steps would have been required to make this change to the original system architecture, and how much more difficult it would have been, especially if you were new to working on the codebase.
Add tire servicing criteria
There are two types of tires currently in use by the Lyft fleet - Carrigan tires and Octoprime tires.
The new tire wear sensors produce an array of four numbers between 0 and 1 inclusive, representing how worn each of the tires are.
This array will be passed to each function in the car factory class, to be used by your tire implementation.
Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
Think carefully about the cleanest way to implement the new tire service criteria, then modify the system to complete the change.
