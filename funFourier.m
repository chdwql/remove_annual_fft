function y_fit=funFourier(y,m)
%��һ�����ݽ��и������,yΪ�������ݣ�mΪ��Ͻ���
N=length(y);
x=1:N;
L=x(end)-x(1);% LΪ��������ĳ���
y=y';
for n=1:m
    bn(n)=(2/L)*trapz(x,y.*sin(2*n*pi*x/L));
    an(n)=(2/L)*trapz(x,y.*cos(2*n*pi*x/L));
end
a0=1/L*trapz(x,y);
%----------------��ʾͼ��----------
x_fit=linspace(x(1),x(end),N);
y_fit=zeros(size(x_fit));
for n=1:m
    y_fit=y_fit+bn(n)*sin(2*n*pi/L*x_fit)+an(n)*cos(2*n*pi/L*x_fit);
end
y_fit=(y_fit+a0)';
end
