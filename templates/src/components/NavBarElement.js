import React, {Component} from "react";


class NavBarElement extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (<div className="NavBarElement">
            <a><div>{this.props.text}</div></a>
        </div>)
    }
}

export default NavBarElement;