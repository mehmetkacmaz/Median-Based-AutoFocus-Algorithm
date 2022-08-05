%% Find best focus point by changing heigth value based on image gradient
function [best_point] = find_best_focus_point(threshold_for_elimination)
resimler = dir('*.bmp');

for i=15%1:numel(resimler)
    im = imread(fullfile(resimler(i).name));
    [im_desired] = eliminate_small_objects(im,250);
    [Gmag,Gdir] = imgradient(im_desired,'sobel');
    Gmag(Gmag==0) = []; % resimdeki 0 olan bölgeleri temizliyoruz ki sadece değişim olan yerler kalsın
    ortanca_deger = median(Gmag);
    ortanca_deger3 = ortanca_deger*3; %3 mediandan büyükler anlamlidir
    Gmag(Gmag<ortanca_deger3) = 0;
    toplam(i) = sum(Gmag); 
end
%%