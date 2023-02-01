# Contest 210 Problem 1 from leet Code
> https://www.youtube.com/watch?v=zrOIQEN3Wkk

> https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbk9GXzc0ellkNG9vd2s0dDJ2RFdPRFc3bnhud3xBQ3Jtc0tueGw4X05ra29UbE11WkhmZEg1UG82TWhwTDBvM1h6LTMtaGhQaWhGTWs0a2tvbmdQQUZHbnZqWGJrM3lVbC1QczVWSW9sYUwtWFEweExWUkdiWE02UG5kVi1xWC1oQzkwMjZPT25mbXpLX1pfV3g1UQ&q=https%3A%2F%2Fleetcode.com%2Fproblems%2Fmaximum-nesting-depth-of-the-parentheses%2F&v=zrOIQEN3Wkk

A string is a valid parentheses string (denoted VPS ) if it meets one of the following:
* it is an emtpy string `""`, or a single character not equal to `"("` or `")"`,
* it can be written as `AB` ( `A` concatenated with `B`), where `A` and `B` are VPS's, or
* it can be written as `(A)`, where `A is a VPS.

We can similarily define the nesting depth `depth(S)` of any VPS `S` as follows:
* `depth("") = 0`
* `depth(A + B) = max(depth(A), depth(B))`, where A and B are VPS's
* `depth("("+ A + ")") = 1 + depth(A)`, where A is a VPS

For example, `""`, `"()()"` are VPS's (with nesting depths 0,1, and 2) and `")("` and `"(()"` are not VPS's.

Given a VPS respresented as string `s`, return the nesting depth of `s`.