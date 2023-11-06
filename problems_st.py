import streamlit as st
from cyllene import ProbStack
from cyllene.MathProblems.problem_parametermultchoice import MultipleChoiceParameterProblem
from cyllene.user.problem_cmds import make_problem
import random

st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

problems = []

problems.append(r"""
Question
<eqn>
D = pickone(0.1,0.2,0.25,0.5);
E = int(1/D);
fracD = line_fraction(Rational(100*D,100));
A = 10*randnum(2,9,1);
B = A*randnum(2,5,1,E);
C = randnum(2,9,1,B/A - 1);
BA = int(B/A);
BA1 = B/A - 1;
BA1C = line_fraction(Rational(BA1,C));
F = line_fraction(Rational(C,BA1));
EQNS = [C, D];
''</eqn>

<watex>
If \[\dfrac{$B}{1 + ${C}e^{-${D}t}} = $A\], solve for \[t\]. &emsp;&emsp;&emsp;&emsp;&emsp; 
</watex>

<_>

Answer
<watex>\[t = $E\ln($F)\]</watex>
<watex>\[t = $E\ln($BA1C)\]</watex>
<watex>\[t = $BA\ln($BA1C)\]</watex>
<watex>\[t = $BA\ln($E)\]</watex>
<watex>\[t = $BA\ln($D)\]</watex>


Solution
<watex>
We can solve for \[t\] in the following manner.  First, multiply both sides of the given equation by \[1 + $EQNS[0]e^{-$EQNS[1]t}\]
<br><br>
<center>\[$B = $A(1 + $EQNS[0]e^{-$EQNS[1]t})\]</center>
<br>
Next, divide both sides by \[$A\].
<br><br>
<center>\[$BA = 1 + $EQNS[0]e^{-$EQNS[1]t}\]</center>
<br>
Next, subtract \[1\] from both sides.
<br><br>
<center>\[$BA1 = $EQNS[0]e^{-$EQNS[1]t}\]</center>
<br>
Next, divide both sides by \[$C\].
<br><br>
<center>\[$BA1C = e^{-$EQNS[1]t}\]</center>
<br>
Next, take the natural logarithm of both sides.
<br><br>
<center>\[\ln($BA1C) = -$EQNS[1]t\]</center>
<br>
And lastly, divide both sides by \[-$D\].
<br><br>
<center>\[ 
t 
= -\dfrac{\ln($BA1C)}{$D} 
= -\dfrac{\ln($BA1C)}{$fracD} 
= -$E\ln($BA1C) 
= $E\ln($F)  \quad \text{ since} -\ln(A) = \ln(1/A) \text{ for all } A > 0
\]</center>
<br>
</watex>

Info
'tags': ["exponential function", "exponential equations", "logarithm"],
'title': "Solve for t",
'id': "3556706_0"
""")

problems.append(r"""
Question
<eqn>
r = randnum(2,9,1);
P = 1000*randnum(2,9,1,r);
PP = commas(P);
t = randnum(2,9,1,r);
EQNS = [PP, r*t/100, 1 + r/100, r*t, r*t/10, r/100];
''</eqn>

<watex>
If \$$PP is invested at \[$r%\] compounded continuously, what will be the accumulated amount after \[$t\] years?
</watex>

<_>

Answer
<watex>\$\[$EQNS[0]e^{$EQNS[1]}\]</watex>
<watex>\$\[$PP($EQNS[2])^{$t}\]</watex>
<watex>\$\[$EQNS[0]e^{$EQNS[3]}\]</watex>
<watex>\$\[$EQNS[0]e^{$t}\]</watex>
<watex>\$\[$EQNS[0]e^{$EQNS[4]}\]</watex>


Solution
<watex>
Since interest is compounded continuously, use the Continuous Compound Interest Formula to compute the accumulated amount:
<br><br>
<center>\[A = Pe^{rt}\]</center>
<br>
where
<br><br>
- \[A\] is the accumulated amount at the end of \[t\] years <br>
- \[P\] is the principal investment (\[P = $PP\]) <br>
- \[r\] is the annual interest rate (\[r = $EQNS[5]\]) <br>
- \[t\] is the term (in years) of the investment (\[t = $t\]) <br>
</watex>

Info
'tags': ["exponential function", "future value"],
'title': "Find the accumulated capital",
'id': "3436899_0"
""")

problems.append(r"""
Question
<eqn>
INDEX = randnum(1,3,1);
period = ['annually','semiannually', 'quarterly', 'monthly', 'daily'];
m = [1,2,4,12,365];
P = 1000*randnum(2,5,1); 
PP = commas(P);
A = P*randnum(2,9,1); 
AA = commas(A); 
AP = A/P;
t = randnum(3,9,1);
mt = m[INDEX]*t;
EQNS = [m[INDEX]];
''</eqn>

<watex>
Find the interest rate \[r\] needed for an investment of \$$PP to grow to \$$AA in $t years if interest is compounded $period[$INDEX].
</watex>

<_>

Answer
<watex>\[r = $EQNS[0]($AP^{1/$mt} - 1)\]</watex>
<watex>\[r = $AP^{1/$mt} + 1\]</watex>
<watex>\[r = $AP^{$mt} - 1\]</watex>
<watex>\[r = $EQNS[0]($AP^{$mt} + 1)\]</watex>
<watex>\[r = $AP^{$mt} + 1\]</watex>


Solution
<watex>
Recall the Compound Interest Formula:
<br><br>
<center>\[A = P\left(1 + \dfrac{r}{m}\right)^{mt}\]</center>
<br>
where
<br><br>
- \[A\] is the accumulated amount at the end of \[t\] years (\[A = $AA\]) <br>
- \[P\] is the principal investment (\[P = $PP\]) <br>
- \[r\] is the nominal interest rate  <br>
- \[m\] is the number of conversion periods per year (\[m = $EQNS[0]\])  <br>
- \[t\] is the term (in years) of the investment (\[t = $t\]) <br>
<br>
Therefore, 
<br><br>
<center>\[$A = ${P}\left(1 + \dfrac{r}{$EQNS[0]}\right)^{$EQNS[0]*$t}\]</center>
<br>
Divide both sides by \[$P\].
<br><br>
<center>\[$AP = \left(1 + \dfrac{r}{$EQNS[0]}\right)^{$mt}\]</center>
<br>
Raise both sides to the \[1/$mt\] power.
<br><br>
<center>\[$AP^{1/$mt} = 1 + \dfrac{r}{$EQNS[0]}\]</center>
<br>
Subtract \[1\] from both sides.
<br><br>
<center>\[$AP^{1/$mt} - 1 = \dfrac{r}{$EQNS[0]}\]</center>
<br>
And finally, multiply both sides by \[$EQNS[0]\].
<br><br>
<center>\[$EQNS[0]($AP^{1/$mt} - 1) = r\]</center>
</watex>

Info
'tags': ["exponential function", "interest rate"],
'title': "Find the interest rate",
'id': "3556708_0"
""")

problems.append(r"""
Question
<eqn>
INDEX = randnum(1,3,1);
period = ['annually','semiannually', 'quarterly', 'monthly', 'daily']
m = [1,2,4,12,365]
mm = m[INDEX];
r = m[INDEX]*randnum(2,5,1); 
rr = r/100; 
rrm = rr/m[INDEX]; 
rrm1 = 1 + rrm;
P = 1000*randnum(2,5,1); 
PP = commas(P);
A = 1000*randnum(6,9,1); 
AA = commas(A);
AP = line_fraction(A,P);
PA = line_fraction(P,A);
EQNS = [mm];
''</eqn>

<watex>
How long will it take for \$$PP to grow to \$$AA if the investment earns an interest rate of \[r\%\] per year compounded $period[$INDEX]?
</watex>

<_>

Answer
<watex>\[\dfrac{\ln($AP)}{$mm\ln($rrm1)}\] years</watex>
<watex>\[\dfrac{$mm\ln($PA)}{\ln($rrm1)}\] years</watex>
<watex>\[\dfrac{$mm\ln($AP)}{$rrm1}\] years</watex>
<watex>\[\dfrac{\ln($AP)}{\ln($rrm1)}\] years</watex>
<watex>\[\dfrac{\ln($PA)}{$mm\ln($rrm1)}\] years</watex>


Solution
<watex>
Recall the Compound Interest Formula:
<br><br>
<center>\[A = P\left(1 + \dfrac{r}{m}\right)^{mt}\]</center>
<br>
where
<br><br>
- \[A\] is the accumulated amount at the end of \[t\] years (\[A = $AA\])
- \[P\] is the principal investment (\[P = $PP\])
- \[r\] is the nominal interest rate (\[r = $rr\])
- \[m\] is the number of conversion periods per year (\[m = $mm\])
- \[t\] is the term (in years) of the investment
</center>
<br>
Therefore, 
<br><br>
<center>\[
$A 
= ${P}\left(1 + \dfrac{$rr}{$mm}\right)^{$EQNS[0]t}
= ${P}(1 + $rrm)^{$EQNS[0]t}
= ${P}($rrm1)^{$EQNS[0]t}
\]</center>
<br>
Divide both sides by \[$P\].
<br><br>
<center>\[$AP = ($rrm1)^{$EQNS[0]t}\]</center>
<br>
Take the natural logarithm of both sides and simplify the right-hand side.
<br><br>
<center>\[
\ln($AP) 
= \ln($rrm1)^{$EQNS[0]t} 
= $EQNS[0]t*\ln($rrm1) 
\]</center>
<br>
And finally, divide both sides by \[$mm\ln($rrm1)\].
<br><br>
<center>\[\dfrac{\ln($AP)}{$mm\ln($rrm1)} = t\]</center>
<br>
</watex>

Info
'tags': ["exponential function", "length of time", "interest", "discrete compounding"],
'title': "Length of time",
'id': "3436900_0"
""")

problems.append(r"""
Question
<eqn>
INDEX = randnum(1,3,1);
(gender) = pickone('him','her');
period = ['annually','semiannually', 'quarterly', 'monthly', 'daily'];
m = [1,2,4,12,365];
r = m[INDEX]*randnum(2,4,1);
P = 5000*randnum(1,3,1,r);
PP = commas(P);
t = randnum(2,9,1,r);
''</eqn>

<watex>
You have \$$PP in the bank comfortably earning \[$r\]\% interest compounded <EQN $period[$INDEX]>. Your cousin needs \$$PP to buy a new car. In order to get the same total return, what interest rate \[r\] should you request from <EQN $gender> if the money you lend <EQN $gender> is to be compounded continuously?
</watex>

<_>

Answer
<watex>\[r = <EQN $m[$INDEX]>\ln(<EQN 1 + $r/100/$m[$INDEX]>)\]</watex>
<watex>\[r = <EQN $m[$INDEX]>\ln(<EQN 1 + $r/100>)\]</watex>
<watex>\[r = (<EQN 1 + $r/100/$m[$INDEX]>)^{<EQN $m[$INDEX]>}\]</watex>
<watex>\[r = <EQN $m[$INDEX]>e^{\ln(<EQN 1 + $r/100/$m[$INDEX]>)}\]</watex>
<watex>\[r = e^{<EQN $m[$INDEX]>\ln(<EQN 1 + $r/100/$m[$INDEX]>)}\]</watex>


Solution
<watex>
The problem suggests that you have two different ways to invest your money: either leave it in the bank earning \[$r%\] interest compounded <EQN $period[$INDEX]> or give it to your cousin and let <EQN $gender> repay you with interest (compounded continuously) in \[t\] years.  (Note that the problem doesn't state when your cousin will repay the loan, however we will see in the following calculations, that the value of \[t\] does not affect the interest rate.)  The problem then is to find the interest rate, \[r\], you should charge your cousin so that you get the same total return regardless of how your money is invested.
<br><br>
If you leave your money in the bank for \[t\] years, then the future value of your investment is
<br><br>
<center>\[P\left(1 + \dfrac{<eqn $r/100>}{<eqn $m[$INDEX]>} \right)^{<eqn $m[$INDEX]>t} = $P(<eqn 1 + $r/100/$m[$INDEX]>)^{<eqn $m[$INDEX]>t}\].</center>
<br>
If you let your cousin borrow your money compounded continuously for \[t\] years, then the future value of your investment (i.e., how much your cousin owes you in \[t\] years) is
<br><br>
<center>\[${P}e^{rt}\]</center>
<br>
where \[r\] is the unknown interest rate.
<br><br>
Now set the two quantities equal to each other and solve for \[r\].
<br><br> 
<center>\[$P(<eqn 1 + $r/100/$m[$INDEX]>)^{<eqn $m[$INDEX]>t} = ${P}e^{rt}\]</center>
<br>
Divide both sides by \[$P\].
<br><br> 
<center>\[(<eqn 1 + $r/100/$m[$INDEX]>)^{<eqn $m[$INDEX]>t} = e^{rt}\]</center>
<br>
Take the natural logarithm of both sides.
<br><br> 
<center>\[\ln((<eqn 1 + $r/100/$m[$INDEX]>)^{<eqn $m[$INDEX]>t}) = ln(e^{rt})\]</center>
<br>
Simplify using properties of logarithms.
<br><br> 
<center>\[<eqn $m[$INDEX]>t\ln(<eqn 1 + $r/100/$m[$INDEX]>) = rt\]</center>
<br>
And finally, divide both sides by \[t\].
<br><br> 
<center>\[<eqn $m[$INDEX]>\ln(<eqn 1 + $r/100/$m[$INDEX]>) = r\]</center>
<br>
</watex>

Info
'tags': ["exponential function", "logarithm", "interest", "continuous compounding", "discrete compounding"],
'title': "Find the interest rate",
'id': "3413483_0"
""")


for p in problems:
    ProbStack.add(make_problem(p, {}, webassign=True))


def write_problem(prob_count: int, prob_key: str):
    st.subheader("Problem " + str(prob_count+1) + ": " +
                 st.session_state.probstack[prob_key].title)
    st.button('New Version', key="new"+str(prob_key),
              on_click=new_problem, args=[prob_key])
    st.write(f"**{st.session_state.probstack[prob_key].statement}**")

    answer = st.radio("Choices",
                      st.session_state.probstack[prob_key].choices,
                      key="radio"+str(prob_key),
                      label_visibility="collapsed")

    if st.button('Submit', type='primary', key="submit"+str(prob_key)):
        if answer == st.session_state.correct[prob_key]:
            st.success('Correct!')
        else:
            st.error('Not quite, please try again.')

    with st.expander("Show Solution"):
        st.write(
            st.session_state.probstack[prob_key].solution, unsafe_allow_html=True)

    st.divider()


def new_problem(prob_key: str):
    st.session_state.probstack[prob_key] = ProbStack.stack[prob_key].get_problem(
    )
    st.session_state.correct[prob_key] = st.session_state.probstack[prob_key].choices[0]
    random.shuffle(st.session_state.probstack[prob_key].choices)


if 'probstack' not in st.session_state:
    st.session_state['probstack'] = {}
    st.session_state['correct'] = {}
    for key, problem in ProbStack.stack.items():
        st.session_state.probstack[key] = problem.get_problem()
        st.session_state.correct[key] = st.session_state.probstack[key].choices[0]
        random.shuffle(st.session_state.probstack[key].choices)


#
# Show problems
#
st.header("Review Problems for Exam 3")

# for key, problem in ProbStack.stack.items():
#     st.write(key, problem)


# st.write(len(st.session_state.probstack))
# loop through problem stack and write
for count, key in enumerate(st.session_state.probstack):
    write_problem(count, key)

#
# write_problem(1)
