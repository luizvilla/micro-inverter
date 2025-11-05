function F = root_Lf_L_Cf(x,Param)

%Param = [Rb, wripple, TDD,r]
%x(1)=Lf
%x(2)=L
%x(3)=Cf

F(1) = x(1)/x(2)-Param(4);
F(2) = (1/(Param(4)*(1-Param(4))*x(2)^2*x(3)))/(Param(2)*(Param(2)^2-1/(Param(4)*(1-Param(4))*x(2)*x(3))))-Param(3)/(50*Param(1));
F(3) = x(2)/x(3)-Param(1)^2;

