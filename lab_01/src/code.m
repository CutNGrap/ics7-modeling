figure('Name', 'Graph 1')
h = 0.01;
x = 1:0.01:7;
a = 2;
b = 5;
a1 = 2;
b1 = 7;
a2 = 1;
b2 = 3;
x = a:h:b;
x1 = 1:h:7;
x2 = 1:h:7;

y = (unifpdf(x,a,b)).*((a <= x) && (x <= b)) + (0)*(x > b) + (0)*(x<a);
plot(x,y, 'LineWidth',2, 'DisplayName','a=2, b=5'), grid;
xlim([0, 7]);
legend;

%%
figure('Name', 'Graph 2')
 plot(x,unifcdf(x,a,b), 'DisplayName','a=2, b=5'), grid;
 hold on;
 plot(x1, unifcdf(x1, a1, b1), 'DisplayName','a=2, b=7');
 hold on;
 plot(x2, unifcdf(x2, a2, b2), 'DisplayName','a=1, b=3');
 legend;
 xlim([0.5, 9.5]);
 ylim([-0.1, 1.1])
 %%
 
MX = 0;
DX = 1;

MX1 = 2;
DX1 = 1;

MX2 = 0;
DX2 = 2;

MX3 = -2;
DX3 = 0.5;
figure('Name', 'Graph 3')
xx = -5:0.01:5;
 plot(xx,normpdf(xx,MX,DX)), grid;
 
 %%
figure ('Name', 'Graph 4')


