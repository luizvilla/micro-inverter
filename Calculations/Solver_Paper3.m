S=450;
Vg=230;
TDD=5;
r=0.75;

Rb=1.613;%Vg^2/S;
wripple=2*pi*10e3;%100e3;

% Rb=Vg^2/S;
% wripple=2*pi*100e3;




Lf_=81.5e-6/3;%590e-6; %Initial value
Lg_=27.2e-6/3;%250e-6; %Initial value
Cf_=41.8e-6/3;%1e-6; %Initial value
% Lf_=590e-6; %Initial value
% Lg_=250e-6; %Initial value
% Cf_=1e-6; %Initial value
L_=Lf_+Lg_;

%x(1)=Lf
%x(2)=L
%x(3)=Cf
options = optimoptions('fsolve','Display','none','PlotFcn',@optimplotfirstorderopt);
options.Display = 'iter';
options.StepTolerance = 1e-9;
options.Algorithm='trust-region-dogleg';
options.MaxFunctionEvaluations = 6e2;
options.MaxIterations = 4.000000e+03;

Param = [Rb, wripple, TDD, r];
fun = @(x)root_Lf_L_Cf(x,Param);

%fun = @root_Lf_L_Cf;
x0 = [Lf_,L_,Cf_];
x = fsolve(fun,x0,options);
%x = fsolve(fun,x0);
Lf=x(1)
Lg=x(2)-x(1)
Cf=x(3)



fun = @(y)root_invL(y,Param);

y = fsolve(fun,L_,options);
Lf2=1/y*r
Lg2=1/y-Lf2
Cf2=(1/y)/Rb^2