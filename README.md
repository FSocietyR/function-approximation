# function-approximation
This tool is a remake of simmilar one
that was created for a school project;

Unseccesfully in  previous version were
problems connected with f*cking everything
starting from strange programm syntax and 
ending on b*llsh*t slow - not optimising - code
(this obviously is not strange, cause progect for
school)

So, previous version was based on linear algebra 
and deriviates ( Jacobian matrix ), by whom 
main function tried to approximate

Attemp I:

    In this v.2 I ll try to, another time, make
    matrix NxN : based on {A, B, C, D, E, F }- variables 
    in Ax^2 +  2Dx + Cy^2 + 2Ey + F = 0;
    It' s logically that the answer, for wich we are looking for,
    should be found 
    in the way : {A/F, C/F, D/F, E/F, 1}

usingv linear algebra we will solve:
    | A' C' D' E' 1   |
    | a1  c1 d1 e1 n1 |
    | a2  c2 d2 e2 n2 | = 0
    | a3  c3 d3 e3 n3 |
    | a4  c4 d4 e4 n4 |
    | a5  c5 d5 e5 n5 |

where I' = I/F, I in {}
    and ai, bi, ci, di, ei, ni = x^2, 2x, y^2, 2y, 1

 So, to write it correctly:

 |A'  |   | a1  a3 a4 a5   |    | -1 |
 |C'  | * | c1 c2 c3 c4 c5 | =  | -1 |
 |D'  |   | d1 d2 d3 d4 d5 |    | -1 |
 |E'  |   | e1 e2 e3 e4 e5 |    | -1 |


So, to say, goal has been achieved,
moreover, now I want to write 
a programm that will make 
not only approximation for 2nd 
order curves but for any dots on a plot
so, i ll try to complete regressions (2nd & 3d)
and least squares method
