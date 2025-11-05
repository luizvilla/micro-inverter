function F = root_invL(x,Param)
%Param = [Rb, wripple, TDD,r]

F=x^3+Param(2)*Param(3)/(50*Param(1))*x^2-Param(4)*(1-Param(4))*Param(3)*Param(2)^3/(50*Param(1)^3);