import torch
from torch.utils.data import TensorDataset, DataLoader


def load_torch_data(load_data_func):
    """Wrapper around load_data to instead use pytorch data loaders."""

    def torch_loader(dataset, data_path, batch_size, shuffle=True, cuda_device=False, num_workers=1):
        (train_data, val_data), (train_labels, val_labels), label_names = load_data_func(dataset, data_path)

        kwargs = {'num_workers': num_workers, 'pin_memory': True} if cuda_device is not None else {}
        kwargs['drop_last'] = True

        train_tensor_data = TensorDataset(torch.from_numpy(train_data), torch.from_numpy(train_labels))
        train_loader = DataLoader(train_tensor_data, batch_size=batch_size, shuffle=shuffle, **kwargs)

        val_tensor_data = TensorDataset(torch.from_numpy(val_data), torch.from_numpy(val_labels))
        val_loader = DataLoader(val_tensor_data, batch_size=batch_size, shuffle=False, **kwargs)

        return train_loader, val_loader, label_names

    return torch_loader

