# PFST
Начальная инструкиця по установке, совпадает с оригинальной. 

### Install Dataset4EO
We use Dataset4EO to handle our data loading. Dataset4EO is a composable data loading package based on TorchData. More information can be found at https://github.com/EarthNets/Dataset4EO.

```shell
git clone https://github.com/EarthNets/Dataset4EO.git
cd Dataset4EO
sh install_requirements.sh
pip install -e .
```
To set up the environment smoothly, we provide the version information of some important packages:
```shell
torch==1.13.1+cu117
torchdata==0.5.1
torchvision==0.14.1
mmcv==1.7.1
```

## Запуск обучения
### Подговока наборов
Наборы данных должны располагаться следующим образом:
```shell
|--dataset_folder
|  |--train
|  |  |--images
|  |  |  |-- # Картинки
|  |  |--gt
|  |  |  |-- # Разметка
|  |--val
|  |  |--images
|  |  |  |-- # Картинки
|  |  |--gt
|  |  |  |-- # Разметка  
```
Разметку необходимо перекрасить. [2,2,2] - цвет воды. [1,1,1] - цвет всего остального

Пути до наборов данных необходимо прописать в конфиге по пути: "configs/_base_/datasets/rucode2RG3.py"
```shell
line 71| data_root_source = 'path to source data'
line 72| data_root_target = 'path to target data'
```
Путь до набора, который используется для финальных предсказаний
```shell
line 104| data_root = 'path to test data'
```

Мы проводили адаптацию между наборами ldalcmix (Смесь landcover и LoveDA) в качестве source набора                                                                                                                                                                     
И набора merged (Смесь картинок train и public) в качестве target
Ссылки на наборы:
(Будут позже)

### Обучение и валидация
Обучение запускается командой:
```shell
python3 tools/train.py configs/pfst/pfst_rucode_RG3_deeplabv3plus_r50-d8.py
```
Валидация на test наборе

```shell
python3 tools/test.py configs/pfst/pfst_rucode_RG3_deeplabv3plus_r50-d8.py work_dirs/path_to_checkpoint --work-dir work_dirs/path_to_dir_with_checkpoint --show-dir test_rucode --revise_checkpoint_key=True --eval='mIoU' --opacity 1
```

Ссылка на нашу модель: 
(Будет позже)

