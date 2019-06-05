function fs_y=funFourierHuaDong(data)
%计算一列日值的滑动年周期
T = 365;        %周期长度
%富氏滑动计算
for i = T:length(data);
    ai = 0;
    for j = i-T+1 : i
        ai = data(j) * cos(2*pi*(j-i+T)/T)+ai;
    end
    fs_y(i) = 2*ai/T;
end
%基波拟合计算
mj=1;   %拟合阶数
nh_y=data(1:365);
y_fit=funFourier(nh_y,mj);      %调用函数计算拟合结果 y_fit：拟合结果
tj=y_fit(365)-fs_y(365);
y_fit2=y_fit-tj;
fs_y=fs_y';
fs_y(1:364)=y_fit2(1:364);      %年周期成分
end
