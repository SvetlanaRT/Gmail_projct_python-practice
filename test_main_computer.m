clear all
close all

 %% Read trajecroty file
fid=fopen('Traj_1.txt','r');
formatSpec = ' %6.1f %6.1';
i=0;
fgetl(fid)
while ~feof(fid)
    i=i+1;
    f=fgetl(fid);
    fnum=str2num(f);
    Data.pos.x(i)=fnum(1);
    Data.pos.y(i)=fnum(2);
end
fclose(fid);



%% const
Data.curr_Pos.x=0;
Data.curr_Pos.y=0;
Data.Const.Obstacle= [30 30];

%% Run
Data=main_computer(Data);

Data.OutPos
