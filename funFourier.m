function y_fit=funFourier(y,m)
%对一列数据进行傅氏拟合,y为输入数据，m为拟合阶数
N=length(y);
x=1:N;
L=x(end)-x(1);% L为定义区间的长度
y=y';
for n=1:m
    bn(n)=(2/L)*trapz(x,y.*sin(2*n*pi*x/L));
    an(n)=(2/L)*trapz(x,y.*cos(2*n*pi*x/L));
end
a0=1/L*trapz(x,y);
%----------------显示图像----------
x_fit=linspace(x(1),x(end),N);
y_fit=zeros(size(x_fit));
for n=1:m
    y_fit=y_fit+bn(n)*sin(2*n*pi/L*x_fit)+an(n)*cos(2*n*pi/L*x_fit);
end
y_fit=(y_fit+a0)';
end
