# This is a Virtual File System
There are several functions you could use:



# Command Specification

## 1. User Registration

### `register [username]`

**Response:**
```
Add `[username]` successfully.
```

**Error:**
- The `[username]` has already existed.
- The `[username]` contains invalid characters.

### Example
Register two users, user1 and user2
```plaintext
# register user1
Add user1 successfully.

# register user2
Add user2 successfully.
```



## 2. Folder Management

## Create a Folder
### `create-folder [username] [foldername] [description]`

**Response:**
```
Create `[foldername]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` contains invalid characters.

### Example
Create a folder for user1 and user2 with the same folder name
```
# create-folder user1 folder1
Create folder1 successfully.
# create-folder user2 folder1
Create folder1 successfully.

# create-folder user1 folder1
Error: folder1 has already existed.
```


## Delete a Folder
### `delete-folder [username] [foldername]`

**Response:**
```
Delete `[foldername]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.



## list folders
### `list-folders [username] [--sort-name|--sort-created] [asc|desc]`

**Response:**
```
List all the folders within the `[username]` scope in the following format:
`[foldername]` `[description]` `[created at]` `[username]`
```

```
**Warning:**
- The `[username]` doesn't have any folders.

**Error:**
- The `[username]` doesn't exist.

```

### Example
List folders for user1 sorted by name in ascending order
```
# list-folders user1 --sort-name asc
folder1 2023-01-01 15:00:00 user1
folder2 this-is-folder-2 2023-01-01 15:00:10 user1
```

## Rename a Folder
### `rename-folder [username] [foldername] [new foldername]`

**Response:**
```
Rename `[foldername]` to `[new-folder-name]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.


## 3. File Management

## Create a file
### `create-file [username] [foldername] [filename] [description]?`

**Response:**
```
Create `[filename]` in `[username]` / `[foldername]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.
- The `[filename]` contains invalid characters.


## Delete a file
### `delete-file [username] [foldername] [filename]`

**Response:**
```
Delete `[filename]` in `[username]` / `[foldername]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.
- The `[filename]` doesn't exist.

## List files
### `list-files [username] [foldername] [--sort-name|--sort-created] [asc|desc]`

**Response:**
```
List files with the following fields:
`[filename]` `[description]` `[created at]` `[foldername]` `[username]`
```

```
**Warning:**
- The folder is empty.

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.
```

### Example
List folders for user1 sorted by name in ascending order
```
file1 this-is-file-1 2023-01-01 15:00:00 folder user1
file2 this-is-file-2 2023-01-01 15:00:10 folder user1
```

## Rename a file
### `rename-file [username] [foldername] [filename] [new filename]`

**Response:**
```
Rename `[filename]` to `[new-file-name]` successfully.
```

**Error:**
- The `[username]` doesn't exist.
- The `[foldername]` doesn't exist.
- - The `[filename]` doesn't exist.


## Note for the usage
The usage for all python files:
```
python register.py [username]

```
If you only want to run

```
register [username]
```
please run the following command:
```
chmod +x register
mv register /usr/local/bin/
```
