function fs_y=funFourierHuaDong(data)
%����һ����ֵ�Ļ���������
T = 365;        %���ڳ���
%���ϻ�������
for i = T:length(data);
    ai = 0;
    for j = i-T+1 : i
        ai = data(j) * cos(2*pi*(j-i+T)/T)+ai;
    end
    fs_y(i) = 2*ai/T;
end
%������ϼ���
mj=1;   %��Ͻ���
nh_y=data(1:365);
y_fit=funFourier(nh_y,mj);      %���ú���������Ͻ�� y_fit����Ͻ��
tj=y_fit(365)-fs_y(365);
y_fit2=y_fit-tj;
fs_y=fs_y';
fs_y(1:364)=y_fit2(1:364);      %�����ڳɷ�
end
