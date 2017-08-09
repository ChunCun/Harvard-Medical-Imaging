data = textread('ndarray.txt','%s');

data2 = [];

for i = 1 : length(data)
    
    a = data(i);
    
    b = str2double(a);
    
    data2 = [data2 ; b];
    
end

data2(isnan(data2))=0;

result_try1 = reshape(data2, [1, 3, 2, 4]);
result_try2 = reshape(data2, [4, 2, 3, 1]);