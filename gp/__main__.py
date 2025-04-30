#!/usr/bin/env python
from pathlib import Path
import argparse

class Gp:
    def __init__(self):
        self.dir = Path(__file__).resolve().parent
        self.dir_temp = self.dir / "templates"
        self.parser = argparse.ArgumentParser(description="Generate a project structure.")
        self.parser.add_argument("name", help="Project name")
        self.parser.add_argument("--path", type=Path, default=Path.cwd(), help="Target directory (default: current directory)")
        self.parser.add_argument("--package", "-p", action="store_true", help="Include __init__.py for package structure")
        args = self.parser.parse_args()
        self.cps(args.name, args.path, args.package)

    def writeFile(self, source: Path, destination: Path) -> None:
        if not source.exists():
            raise FileNotFoundError(f"Template not found: {source}")
        text = source.read_text()
        destination.write_text(text)

    def cps(self, project_name, base_path, package) -> None:
        path = Path(base_path)
        root = path / project_name
        log = root / "logs"

        config = root / "config"
        
        core = root / "core"

        for path in [log, config, core]:
            path.mkdir(parents=True, exist_ok=True)


        # files
        pathfile = Path(config / "path.py")
        pathfiler = Path(self.dir_temp / "pathTemp.py")
        self.writeFile(pathfiler, pathfile)

        # zero file
        zerofile = Path(core / 'zero.py')
        zerofiler = Path(self.dir_temp / 'zeroTemp.py')
        self.writeFile(zerofiler, zerofile)

        # mainfile
        mainfilename = "main.py"
        mainfiletemp = "mainTempNp.py"

        if package: # for packages
            initfile = Path(root / "__init__.py")
            initfiler = Path(self.dir_temp / "initTemp.py")
            self.writeFile(initfiler, initfile)
            mainfilename = "__main__.py"
            mainfiletemp = "mainTempP.py"

        # main file creation
        mainfile = Path(root / mainfilename)
        mainfiler = Path(self.dir_temp / mainfiletemp)
        self.writeFile(mainfiler, mainfile)

        # creating log file for storing the log
        (log / "log.txt").write_text("")

        # README.md File creation code
        readme = Path(root / "README.md")
        readmer = Path(self.dir_temp / "readmeTemp.md") 
        self.writeFile(readmer, readme)

        print(f"Project '{project_name}' created at '{root}'")

def main():
    Gp()

# main entry point        
if __name__ == "__main__":
    main()
