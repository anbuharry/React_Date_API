import React, { Component } from 'react'
import axios from 'axios'
class PostForm extends Component {
	constructor(props) {
		super(props)

		this.state = {
			key: '',
			
		}
		console.log(this.state)
	}

	changeHandler = e => {
		this.setState({ [e.target.name]: e.target.value })
	}

	submitHandler = e => {
		e.preventDefault()
		
		axios
		.get(`http://127.0.0.1:8000/hvals_hash?key=${this.state.key}`)
		.then(response => {
			console.log(response)
		})
		.catch(error => {
			console.log(error)
		})
	}

	render() {
		const { key } = this.state
		return (
			<div>
				<form onSubmit={this.submitHandler}>
					<div>
						<input
							type="text"
							name="key"
							value={key}
							onChange={this.changeHandler}
						/>
					</div>

					<button type="submit">Submit</button>
				</form>
			</div>
		)
	}
}



export default PostForm
