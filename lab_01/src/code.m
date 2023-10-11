figure('Name', 'Graph 1')
h = 0.01;
a = 2;
b = 5;
a1 = 1;
b1 = 6;
a2 = 3;
b2 = 5;


x = 0:h:7;

y = unifpdf(x,a1,b1);
plot(x,y, 'LineWidth',2, 'DisplayName','a=1, b=6'), grid;
xlim([0, 7]);
ylim([-0.2, 0.8]);
legend;

figure('Name', 'Graph 2')
 plot(x,unifcdf(x,a1,b1), 'DisplayName','a=1, b=6'), grid;
 legend;
xlim([0, 7]);
ylim([-0.2, 1.2]);
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
 plot(xx,normpdf(xx,MX2,DX2)), grid;
 
 xlim([-5, 5]);
 ylim([0, 1]);
 
 
 
figure ('Name', 'Graph 4')

plot(xx,normcdf(xx,MX2,DX2)), grid;
xlim([-5, 5]);
 ylim([0, 1]);


